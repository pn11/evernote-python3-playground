import argparse

# !pip install evernote3
import evernote.edam.notestore.NoteStore as NoteStore

import login

def main():
    parser = argparse.ArgumentParser(description='Search your note in Evernote')
    parser.add_argument('search_query', help='search query')
    args = parser.parse_args()
    print(args)

    client = login.login()
    user = client.get_user_store().getUser()
    note_store = client.get_note_store()

    # 検索用のフィルター
    filter = NoteStore.NoteFilter()
    # この記法が使える https://dev.evernote.com/doc/articles/search_grammar.php
    #filter.words = "created:month-1 notebook:Note"
    filter.words = args.search_query
    filter.ascending = False

    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True

    ourNoteList = note_store.findNotesMetadata(filter, 0, 100, spec)

    def make_link(user, note):
        return f"https://www.evernote.com/shard/{user.shardId}/nl/{user.id}/{note.guid}"


    for note in ourNoteList.notes:
        print(f"{note.title}: {make_link(user, note)}")


if __name__ == '__main__':
    main()
