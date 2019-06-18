
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.user import User
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adaccountuser import AdAccountUser
from facebook_business.adobjects.campaign import Campaign

keys=[]
#reading file containing keys
with open('secretfb.txt') as file:
	for line in file:
		l = line
		keys.append(l)
app_id= keys[0]
app_secret= keys[1]
token= keys[2]
ad_account_id= keys[3]		

#print(app_id,app_secret,token,ad_account_id)
		
FacebookAdsApi.init(access_token = token)

#Account ID
me=AdAccountUser(fbid='me')
my_account= me.get_ad_accounts()[0]
Account_id = my_account['id']

#initializing accountid to classs object		
class Account(object):
	def __init__(self,account_id):
		self.account_id= account_id
		
new_acc = Account(account_id=  Account_id)

campaigns = my_account.get_campaigns()
print(campaigns)
campaign = Campaign(new_acc.account_id)
params ={ 'data_preset': 'this_year'}

fields=[
		'campaign_name',
		'adset_name',
		'adset_id',
		'impressions',
		'spend',
		'reach',
		'actions',
		'action_values'
		]
	
#getting insights
		
insights = campaign.get_insights(fields, params)
print(insights)
