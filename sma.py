class sms_store:
    def __init__(self):
        self.message = []
        self.viwed_state = []
    def add_new_arrival(self,from_number,time_arrived,text_of_sms):
        self.message.append((from_number,time_arrived,time_arrived))
        self.viwed_state.append(False)
    def message_counts(self):
        return len(self.message)
    def get_unread_indexes(self):
        indices=[]
        for (i,v) in enumerate(self.viwed_state):
            if not v:
                indices.append(i)
            return indices
    def