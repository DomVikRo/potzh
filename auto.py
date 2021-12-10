class Auto:
    """Autók osztálya"""
    def __init__(self,sor:str):
        a=sor.split(" ")
        self.ora=a[0]
        self.perc=a[1]
        self.mp=a[2]
        self.rt=a[3]
    def ora_leker(self)->str:
        return self.ora

    def perc_leker(self)->str:
        return self.perc

    def mp_leker(self)->str:
        return self.mp

    def rt_leker(self)->str:
        return self.rt
