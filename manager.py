from job import Job
import queue


class ContinuousIntegrationManager:
    def __init__(self, number_of_workers: int, max_job_queue_size: int = 10, max_starvation_duration: int = 10):
        self.job_queue = queue.Queue()
        self.job_priorized_queue = queue.Queue()
        self.number_of_workers = number_of_workers
        self.max_job_queue_size = max_job_queue_size
        self.max_starvation_duration = max_starvation_duration

    def process_jobs(self):
        while self.number_of_workers:
            if self.job_priorized_queue.qsize() > 0:
                tamanho = self.job_priorized_queue[self.number_of_workers].get_job()
                self.job_priorized_queue[self.number_of_workers].set_job(tamanho - 1)
                if(tamanho<0):
                    self.job_priorized_queue.get()
            else:
                tamanho = self.job_queue.queue[self.number_of_workers].get_job()
                self.job_queue.queue[self.number_of_workers].set_job(tamanho - 1)
                if (tamanho < 0):
                    self.job_queue.get()

    def add_job(self, project_name: str, job_duration: int, is_prioritized: bool):
      job = Job(project_name,job_duration,is_prioritized)
      if job.is_prioritized():
        self.job_priorized_queue.put(job)
      else:
        self.job_queue.put(job)


    def print_final_report(self):
        print(f'Maximum job queue size reached: {0}')

    def print_current_status(self):
        print(f'Total workers busy/idle: {0}/{0}')
        print(f'Pending jobs: {[]}')
        print(f'Current job per worker: {[]}')
