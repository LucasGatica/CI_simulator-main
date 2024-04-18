class Job:
    def __init__(self, name: str, job: int, is_prioritized: bool):
        self._name = name
        self._job = job
        self._is_prioritized = is_prioritized


    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name


    def get_job(self) -> int:
        return self._job

    def set_job(self, job: int) -> None:
        self._job = job

    def is_prioritized(self) -> bool:
        return self._is_prioritized

    def set_prioritized(self, is_prioritized: bool) -> None:
        self._is_prioritized = is_prioritized
