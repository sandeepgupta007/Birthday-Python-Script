#sandeep_007

'''
	The sole purpose of this code is to comment a thank you message to all the 
	post on your timeline on your birthday with a filter for checking whether the
	post is a bday wish or not.
'''

from urllib.parse import urlparse, parse_qs
from random import choice
import re
from datetime import datetime, date, time
import calendar
import sys
from urllib.parse import urlencode
import urllib
import requests


# Birthdate
''' 
	Though the birthday is on 4 - January but here in india the time will be GMT+5:30
	and facebook stores time in UTC to change it accordingly.
		
	for example: 4 january, India
	than 3 Jan, 18:30 will be UTC for that purpose.	
	
'''
bday = datetime(2018, 1, 2, 18, 30, 0)

'''
	acess token from facebook developer website
'''

access_token = "EAACEdEose0cBAKNjzZA11tzQQG4KbrXwNwS4FDaROSgreWgkGjMtA4awDmici82ptel3ZAaYwlpeiLP4ZAOSfKRi9hBuJWg0e9c1F7ZBNWVIc3HXyEf8uy1iLa2oEFv9h0XUBHpCY18NhZCBVrwMbcjON5ZB9IqCfcZAqd1HSvbZAWVsXyRMgljLfWMyCr0rqvxwnGjnpVlx2QZDZD"

'''
	Set like = True for like the post on Wall
		like = False if not. 
'''
like = True;

comment = True;

''' 
	A message will be randomly selected from mesaage_set

'''
message_set = ['Thanks! :) ','Thank you very much :) ', 'Thanks a lot :) ', 'Thank you! :)']


use_filter = True

# bdaywords list contains the keywords which will be used as a filter while checking a post 
bdaywords = ["happy", "bday", "b\'day", "birthday","hbd", "wish", "returns"]

# converting bday to epoch or Timestamp for UTC
''' 
	1514918235 seconds since Jan 01 1970. (UTC)

	This epoch translates to:

	01/02/2018 @ 6:37pm (UTC) or Tue, 02 Jan 2018 18:37:15 
'''

epoch=datetime(1970,1,1)
td = bday - epoch
utc_bday = int((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6)

#get all the post
def get_posts(url, wishes=None):
    #check if we are done
    if wishes is None:
        wishes = []
        stop = False
    else:
        until = parse_qs(urlparse(url).query).get('until')
        stop = int(until[0]) < utc_bday

    if stop:
        return wishes
    else:
        print(url)
        req = requests.get(url)
        if req.status_code == 200:
            
            content = req.json()
            print (content)
            #keep only relevant fields from post data
            '''feed = []
            for post in content['data']:
                feed.append({'id': post['id'],'from': post['from']['name'],'message': post.get('message', ''),'type': post['type']})

            #keep only posts relevant to birthday. Make sure you reply your friends who post happy birthday pictures on your timeline or posts in local language
            for post in feed:
                if post['type']=='status' and is_birthday(post['message'], use_filter) :
                    wishes.append(post)
            print (content) '''
            #next_url = content['paging']['next']
            return wishes
            #return get_posts(next_url, wishes)
        else:
            print ("Unable to connect. Check if session is still valid")

def confirm():
	print('Confirm')
	while(True):
		ans = input()
		if not ans:
		    return False
		if ans not in ['y', 'Y', 'n', 'N']:
		    print ('please enter y or n.')
		    continue
		if ans == 'y' or ans == 'Y':
		    return True
		if ans == 'n' or ans == 'N':
		    return False

def is_birthday (message, filter):
    if filter == False:
        return True
    for keyword in bdaywords:
        if keyword in message:
            return True
    return False

if __name__ == '__main__':
    
    #get bithday wishes
    base_url = 'https://graph.facebook.com/v2.11/me/feed'
    params = {'since': utc_bday, 'access_token': access_token}
    url = '%s?%s' % (base_url, urlencode(params))
    posts = get_posts(url)
    
    #confirm before posting
	#d = len(posts)
	#print (posts)
	#print("Found %s birthday wishes, Ready to thank them?"%len(posts))
    usersignal = confirm()
    
    #post if user said yes
    '''
	if usersignal is True:
        for post in posts:

            #thank the user
            if comment:
                reply = choice(message_set)
                print 'Replying %s to %s' % (reply, wish['from'])
                url = 'https://graph.facebook.com/%s/comments?access_token=%s' % (wish['id'], access_token)
                requests.post(url, data={'message': reply})

            if like:
                url = 'https://graph.facebook.com/%s/likes?access_token=%s' % (wish['id'], access_token)
                requests.post(url, data="") 
	'''
