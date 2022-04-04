class Save:

    @staticmethod
    def save(*args):
        save = open('save.txt', 'w', encoding="utf-8")
        for data in args:
            save.write(f'{data}\n')
        save.close()
