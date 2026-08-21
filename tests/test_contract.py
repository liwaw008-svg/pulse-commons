import ast,pathlib
P=pathlib.Path(__file__).parents[1]/'contracts'/'contract.py';S=P.read_text(encoding='utf-8')
def allocate():
 n=next(x for x in ast.parse(S).body if isinstance(x,ast.FunctionDef) and x.name=='fair_allocate');z={};exec(compile(ast.Module([n],[]),str(P),'exec'),z);return z['fair_allocate']
def test_surface():ast.parse(S);assert all(x in S for x in ('open_epoch','close_epoch','get_epoch','run_nondet_unsafe'))
def test_never_exceeds_capacity():
 out=allocate()(7,[{'label':'a','eligible':True,'requested':9},{'label':'b','eligible':True,'requested':6}]);assert sum(x['allocated'] for x in out)==7
def test_ineligible_claim_gets_nothing():assert allocate()(10,[{'label':'a','eligible':False,'requested':10}])==[]
def test_small_demand_is_fully_served():assert allocate()(10,[{'label':'a','eligible':True,'requested':4}])==[{'label':'a','allocated':4}]
def test_caller_amounts_removed():assert 'requested:list[u256]' not in S and 'Fetched pulse records in matching order:' in S
