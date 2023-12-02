from api.chehra.utils import UniqueIdGenerator



#watch neetcode :you can use singleton pattern to hold the state of your uuid
class ChehraStartupHandler:
    instance = None 
    def __init__(self):
        # self.initialize_uuid_generator()
        self.curr_uuid = 0

    # @classmethod
    # def initialize_uuid_generator(cls):
    #     table = "embeddingStore"
    #     cls.uuid_generator = UniqueIdGenerator(table)

    @staticmethod
    def get_curr_instance():
        if not ChehraStartupHandler.instance:
            ChehraStartupHandler.instance = ChehraStartupHandler() 
            
        return ChehraStartupHandler.instance

def return_last_uuid_from_db():
    table = "embeddingStore"
    uuid_generator = UniqueIdGenerator(table)
    return uuid_generator.last_uuid_saved() 

