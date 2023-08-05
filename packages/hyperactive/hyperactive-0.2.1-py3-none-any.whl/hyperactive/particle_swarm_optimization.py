# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


import random

import numpy as np
import tqdm

from .base import BaseOptimizer
from .search_space import SearchSpace


class ParticleSwarm_Optimizer(BaseOptimizer):
    def __init__(
        self,
        search_config,
        n_iter,
        metric="accuracy",
        memory=None,
        n_jobs=1,
        cv=5,
        verbosity=1,
        random_state=None,
        warm_start=False,
        n_part=1,
        w=0.5,
        c_k=0.5,
        c_s=0.9,
    ):
        super().__init__(
            search_config,
            n_iter,
            metric,
            memory,
            n_jobs,
            cv,
            verbosity,
            random_state,
            warm_start,
        )

        self.n_part = n_part
        self.w = w
        self.c_k = c_k
        self.c_s = c_s

        self.best_score = 0
        self.best_pos = None

        self.search_space_inst = SearchSpace(warm_start, search_config)

    def _find_best_particle_score(self, p_list):
        for p in p_list:
            if p.best_score > self.best_score:
                self.best_score = p.best_score
                self.best_pos = p.best_pos

    def _find_best_particle_loss(self, p_list):
        for p in p_list:
            if p.best_score < self.best_score:
                self.best_score = p.best_score
                self.best_pos = p.best_pos

    def _init_particles(self):
        p_list = [Particle() for _ in range(self.n_part)]
        for p in p_list:
            p.max_pos_list = self.max_pos_list
            p.pos = self.search_space_inst.pos_dict2np_array(
                self.search_space_inst.get_random_position()
            )
            p.best_pos = self.search_space_inst.pos_dict2np_array(
                self.search_space_inst.get_random_position()
            )
            p.velo = np.zeros(self._get_dim_SearchSpace())

        return p_list

    def _get_dim_SearchSpace(self):
        return len(self.search_space_inst.search_space)

    def _limit_pos(self, search_space):
        max_pos_list = []
        for values in list(search_space.values()):
            max_pos_list.append(len(values) - 1)

        self.max_pos_list = np.array(max_pos_list)

    def _move_particles(self, p_list):

        for p in p_list:
            A = self.w * p.velo
            B = self.c_k * random.random() * np.subtract(p.best_pos, p.pos)
            C = self.c_s * random.random() * np.subtract(self.best_pos, p.pos)
            new_velocity = A + B + C

            p.velo = new_velocity
            p.move()

    def _eval_particles_score(self, p_list, X_train, y_train):
        for p in p_list:
            hyperpara_dict = self.search_space_inst.pos_np2values_dict(p.pos)
            p.score, _, p.sklearn_model = self.model.train_model(
                hyperpara_dict, X_train, y_train
            )
            if p.score > p.best_score:
                p.best_score = p.score
                p.best_pos = p.pos

    def _eval_particles_loss(self, p_list, X_train, y_train):
        for p in p_list:
            hyperpara_dict = self.search_space_inst.pos_np2values_dict(p.pos)
            p.score, _, p.sklearn_model = self.model.train_model(
                hyperpara_dict, X_train, y_train
            )
            if p.score < p.best_score:
                p.best_score = p.score
                p.best_pos = p.pos

    def _search(self, n_process, X_train, y_train):
        hyperpara_indices = self._init_search(n_process, X_train, y_train)

        self._limit_pos(self.search_space_inst.search_space)

        self._set_random_seed(n_process)
        self.n_steps = self._set_n_steps(n_process)

        hyperpara_dict = self.search_space_inst.pos_dict2values_dict(hyperpara_indices)
        self.best_pos = self.search_space_inst.pos_dict2np_array(hyperpara_indices)
        self.best_score, train_time, sklearn_model = self.model.train_model(
            hyperpara_dict, X_train, y_train
        )

        p_list = self._init_particles()

        for i in tqdm.tqdm(
            range(self.n_steps),
            desc=str(self.model_str),
            position=n_process,
            leave=False,
        ):

            if self.metric_type == "score":
                self._eval_particles_score(p_list, X_train, y_train)
                self._find_best_particle_score(p_list)
            elif self.metric_type == "loss":
                self._eval_particles_loss(p_list, X_train, y_train)
                self._find_best_particle_loss(p_list)

            self._move_particles(p_list)

        best_hyperpara_dict = self.search_space_inst.pos_np2values_dict(self.best_pos)
        score_best, train_time, sklearn_model = self.model.train_model(
            best_hyperpara_dict, X_train, y_train
        )

        start_point = self._finish_search(best_hyperpara_dict, n_process)

        return sklearn_model, score_best, start_point


class Particle:
    def __init__(self):
        self.pos = None
        self.velo = None
        self.score = None

        self.best_pos = None
        self.best_score = 0

        self.sklearn_model = None

        self.max_pos_list = None

    def move(self):
        self.pos = (self.pos + self.velo).astype(int)

        zeros = np.zeros(len(self.pos))
        self.pos = np.maximum(self.pos, zeros)
        self.pos = np.minimum(self.pos, self.max_pos_list)
