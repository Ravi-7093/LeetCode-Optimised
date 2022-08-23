class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        ans=0
        hours = 0
        if(initialEnergy < 0 or initialExperience < 0):
            return 0
        if(len(energy) == 0 or len(experience) == 0):
            return 0
        for i in range(len(energy)):
            if(initialEnergy <= energy[i]):
                hours += (energy[i]-initialEnergy)+1
                initialEnergy += (energy[i]-initialEnergy)+1

            if(initialExperience <= experience[i]):
                hours += (experience[i]-initialExperience)+1
                initialExperience += (experience[i]-initialExperience)+1

            initialEnergy -= energy[i]
            initialExperience += experience[i]
        return hours
       
