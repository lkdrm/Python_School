class Context:
    def __init__(self):
        pass

    def __enter__(self):
        print("Oteviram context management.")
        return self

    def __exit__(self,exc_type,exc_value,exc_traceback):
        print("Zaviram context management...")

with Context():
    print("Tohle je uprosted ... napr. kdyz zapisuji do souboru...")
 