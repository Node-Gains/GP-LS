class ls:
    #propiedades de la especiacion
    #cambio para neat

    def descendents(self, des):
        self.descendent=des

    def get_descendents(self):
        return self.descendent

    def LS_probability(self, ps):
        self.LS_prob=ps

    def get_LS_prob(self):
        return self.LS_prob

    def params_set(self, params):
        self.params=params

    def get_params(self):
        return self.params

    def LS_applied_set(self, value):
        self.ls_ind=value

    def LS_applied_get(self):
        return self.ls_ind

    def LS_fitness_set(self,value):
        self.ls_fitness=value

    def LS_fitness_get(self):
        return self.ls_fitness

    def LS_story_set(self, value):
        self.ls_story=value

    def LS_story_get(self):
        return self.ls_story

    def off_cx_set(self, value):
        self.off_cx=value

    def off_cx_get(self):
        return self.off_cx

    def off_mut_set(self, value):
        self.off_mut=value

    def off_mut_get(self):
        return self.off_mut

    def binary_rep_get(self):
        return self.repr_bin

    def binary_rep_set(self, value):
        self.repr_bin=value

    def binary_level_get(self):
        return self.level_bin

    def binary_level_set(self, value):
        self.level_bin=value

    def nodefeat_get(self):
        return self.node_feat


class pop_param:
    def save_ind(self):
        return True
