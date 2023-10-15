class TaillardInstance:

    def __init__(self, type, seed, durations, machine_assignments=None):

        self.number_machines = 0
        self.number_jobs = 0

        self.type = type
        self.seed = seed
        self.durations = durations
        self.machine_assignments = machine_assignments
        self.lower_bound = self._calculate_lower_bound(type, durations,)

    def _calculate_lower_bound(self, type, durations):
        pass


