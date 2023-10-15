from taillard_instance_tools.TaillardRNG import TaillardRNG


class TaillardInstanceGenerator:
    def __init__(self, time_rng, machine_rng):

        self._time_rng = time_rng
        self._machine_rng = machine_rng

    def generate_flowshop(self, m, n):
        """
        Generate a flowshop instance with m machines and n jobs.
        :param m: Number of machines.
        :param n: Number of jobs.
        :return: A list of lists representing the processing times for each job on each machine.
        """

        d = self._generate_processing_times(m, n)

        # b = [min(d[i][j] for j in range(n)) for i in range(m)]
        # a = [min(sum(d[i][j] for i in range(k + 1)) for k in range(m)) for j in range(n)]
        # T = [sum(d[i][j] for j in range(n)) for i in range(m)]

        # Lower bound for the makespan
        #LB = max(max(b[i] + T[i] + a[i] for i in range(m)), max(sum(d[i][j] for i in range(m)) for j in range(n)))

        return d

    def generate_job_and_open_shop(self, m, n):
        """
        Generate a job or openshop instance with m machines and n jobs.
        :param m: Number of machines.
        :param n: Number of jobs.
        :return: A tuple of lists of lists representing the processing times and machine assignements for each job on each machine.
        """
        # Step 1: Generate processing times d_ij
        d = self._generate_processing_times(m, n)

        # Step 2: Initialize machine assignments M_ij
        M = [[i for i in range(m)] for _ in range(n)]

        # Step 3: Randomly swap machine assignments
        for j in range(n):
            for i in range(m):
                i_rand = self._machine_rng.next_int(0, m - 1)  # Random machine index
                M[j][i], M[j][i_rand] = M[j][i_rand], M[j][i]

        return d, M

    def _generate_processing_times(self, m, n):
        return [[self._time_rng.next_int(1, 99) for _ in range(m)] for _ in range(n)]


if __name__ == '__main__':
    number_jobs = 2
    number_machines = 2

    time_seed = 840612802
    machine_seed = 398197754

    time_rng = TaillardRNG()
    machine_rng = TaillardRNG()
    generator = TaillardInstanceGenerator(time_rng, machine_rng)

    number_instances = 5000
    generated_instances = []
    for i in range(number_instances):
        jobshop = generator.generate_job_and_open_shop(number_machines, number_jobs)
        generated_instances.append(jobshop)

    from copy import deepcopy

    generated_instances.append(deepcopy(jobshop))

    converted_jobshops = [(tuple(tuple(i) for i in a), tuple(tuple(j) for j in b)) for a, b in generated_instances]
    unique_jobshops = set(converted_jobshops)
    num_unique = len(unique_jobshops)
    num_duplicates = len(generated_instances) - num_unique
    pass
