import pymongo

def getCollection():
    client = pymongo.MongoClient('mongodb+srv://pranav:AbTRl9cqEWwnrzSo@cluster0.4jlb79c.mongodb.net/?retryWrites=true&w=majority')
    #Define DB Name
    dbname = client['jobDetails']

    #Define Collection
    collection = dbname['pythonDeveloperJobs']

    return collection

if __name__ == "__main__":   
    dbname = getCollection()