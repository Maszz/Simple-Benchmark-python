class TimeConverter():
    def __init__(self, seconds):
        """
        Setup constants units. 
        and other setup format.
        """
        self.SECONDS_OF_HOURS = 3600
        self.SECONDS_OF_MINUTES = 60
        self.timeFormat = self.timeConverter(seconds)

    def toString(self):
        """
        To string of class.
        :param: none
        :return: str
        """
        return f'{self.timeFormat[0]} Hrs {self.timeFormat[1]} Min {self.timeFormat[2]:.0f} Sec {self.timeFormat[3]:.0f} ms \n'

    def toShortString(self):
        return f'{self.timeFormat[1]} : {self.timeFormat[2]:.0f} : {self.timeFormat[3]:.0f} \n'

    def timeConverter(self, second):
        """     
        This function calculates time in seconds to %H %M %S %MS
        :param : seconds.
        :return : truple of time : (H,M,S,MS).
        """

        seconds = second

        hour, minnite = 0, 0

        if seconds >= self.SECONDS_OF_HOURS:
            hour += seconds // self.SECONDS_OF_HOURS
            seconds = seconds % self.SECONDS_OF_HOURS
        if seconds >= self.SECONDS_OF_MINUTES:
            minnite += seconds // self.SECONDS_OF_MINUTES
            seconds = seconds % self.SECONDS_OF_MINUTES

        if seconds < 1:
            millisecond = seconds * 1000
            seconds = 0

        else:
            millisecond = ((seconds*10) % 10)*1000 / 10
            seconds = (seconds*10)//10

        return (hour, minnite, seconds, millisecond)
