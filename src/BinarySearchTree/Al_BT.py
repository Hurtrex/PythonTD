class Al_BT:
    def __init__(self):
        self.bt = ArrayList()

    def find(self, data):
        for i in range(self.bt.len()):
            if self.bt[i] == data:
                return i

        return -1

    def add(self,data,parent_data,direction):
        if self.bt.len() == 0:
            self.bt[0] = data
            return
        p_index = self.find(parent_data)
        if p_index >= 0:
            if direction == "left":
                self.bt[2 * p_index + 1] = data
            if direction == "right":
                self.bt[2 * p_index + 1] = data