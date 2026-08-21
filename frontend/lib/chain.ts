import { createAccount, createClient } from 'genlayer-js';
import { testnetBradbury } from 'genlayer-js/chains';

export const CONTRACT = (process.env.NEXT_PUBLIC_CONTRACT_ADDRESS || '0x0000000000000000000000000000000000000000') as `0x${string}`;
export const EXPLORER = 'https://explorer-bradbury.genlayer.com/transactions';
const endpoint = 'https://rpc-bradbury.genlayer.com';
const reader:any = createClient({ chain:testnetBradbury, endpoint, account:createAccount() });
let signer:any;

export async function connect(){
 const provider:any=(window as any).ethereum;
 if(!provider) throw new Error('Install Rabby or MetaMask first.');
 const [address]=await provider.request({method:'eth_requestAccounts'});
 if((await provider.request({method:'eth_chainId'})).toLowerCase()!=='0x107d') await provider.request({method:'wallet_switchEthereumChain',params:[{chainId:'0x107d'}]});
 signer=createClient({chain:testnetBradbury,endpoint,account:address,provider});
 return address as string;
}
export async function read(name:string,args:any[]=[]){if(CONTRACT.endsWith('0000000000000000000000000000000000000000'))throw new Error('Contract deployment is pending.');return reader.readContract({address:CONTRACT,functionName:name,args});}
export async function write(name:string,args:any[]=[]){if(!signer)throw new Error('Connect wallet first.');if(CONTRACT.endsWith('0000000000000000000000000000000000000000'))throw new Error('Contract deployment is pending.');const hash=await signer.writeContract({address:CONTRACT,functionName:name,args,value:0n});await signer.waitForTransactionReceipt({hash,status:'ACCEPTED',retries:120,interval:5000});return hash as string;}
