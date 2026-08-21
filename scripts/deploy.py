import json,os,re
from genlayer_py import create_client,create_account
from genlayer_py.chains import testnet_bradbury
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));W=os.path.abspath(os.path.join(R,'..','..','..','..'))
def v(n):return re.search(rf'^\s*{n}\s*=\s*"?([^"\r\n]+)',open(os.path.join(W,'accounts.env'),encoding='utf-8').read(),re.M).group(1).strip()
def f(x):
 if isinstance(x,dict):
  if x.get('recipient') and str(x.get('tx_execution_result',''))=='1':return x['recipient']
  for z in x.values():
   r=f(z)
   if r:return r
 if isinstance(x,list):
  for z in x:
   r=f(z)
   if r:return r
 a=create_account(account_private_key=v('ACCOUNT_4_GENLAYER_PRIVATE_KEY'));cl=create_client(chain=testnet_bradbury,account=a);h=cl.deploy_contract(code=open(os.path.join(R,'contracts','contract.py'),encoding='utf-8').read(),args=[]);print('deployTx',h,flush=True);addr=f(cl.wait_for_transaction_receipt(transaction_hash=h,status='ACCEPTED',retries=80,interval=20000));o={'epoch':{'contract':addr,'opening_tx':h},'commons':'Bradbury','host':a.address,'allocation':'ordered-capacity-fill'};open(os.path.join(R,'epoch-anchor.json'),'w').write(json.dumps(o,indent=2));print(json.dumps(o),flush=True)
