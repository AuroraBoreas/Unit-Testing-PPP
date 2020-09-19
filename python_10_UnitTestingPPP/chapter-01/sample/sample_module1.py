class StringLong:
    _wasLastStringLong: bool = False
    def isStringLong(self, s: str) -> bool:
        r = len(s) > 5
        self._wasLastStringLong = r
        return r