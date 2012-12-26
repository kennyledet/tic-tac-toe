import sys, urllib2, json, time

def main():
    board = sys.argv[1].lower()
    query = sys.argv[2].strip('"')
    # Get num of board pages
    boards = json.loads(urllib2.urlopen('http://api.4chan.org/boards.json').read())['boards']
    for _board in boards:
        if _board['board'] == board:
            num_pages = int(_board['pages'])
            break
    # Begin search
    for page in range(0,num_pages):
        print 'Found on page %d:' % (page,)
        threads = json.loads(urllib2.urlopen('http://api.4chan.org/g/%d.json' % (page,)).read())['threads']
        for thread in threads:
            for post in thread['posts']:
                if ('com' in post.keys() and query in post['com']) or ('sub' in post.keys() and query in post['sub']):
                    print 'http://boards.4chan.org/%s/res/%d' % (board, post['no'])
        time.sleep(1)

if __name__ == '__main__':
    main()
