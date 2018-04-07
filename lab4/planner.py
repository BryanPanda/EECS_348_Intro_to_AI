import urllib2, json, sys, os

class Plan(object):
    """ Object representing the results of finding a plan.  If planning is successful, then ok will be true, 
        plan will have the names of the list of actions, and actions will have the full description of each action in the plan

    Attributes:
        ok (boolean): True if a plan is successfully found
        plan (list of strings): Names of each action in the plan
        actions (list of strings): Full description of each action in the plan
        error (string): Error message returned from the planner
    """
    def __init__(self, resp):
        self.ok = (resp['status'] == 'ok')
        if self.ok:
            self.plan = [act['name'] for act in resp['result']['plan']]
            self.actions = [act['action'] for act in resp['result']['plan']]
        else:
            self.error = resp['result']['error']
            self.parse_status = resp['result']['parse_status']

def file_paths(d, p):
    """ Get the fully qualified file paths to the domain and problem files

    Args:
        d (str): name of the domain file
        p (str): name of the problem file
    """
    src_dir = os.path.dirname(os.path.abspath(__file__))
    domain_file = os.path.join(src_dir, d)
    problem_file = os.path.join(src_dir, p)
    return domain_file, problem_file

def find_plan(domain, problem):
    """ Get the plan for the 

    Args:
        domain (str): name of the domain file
        problem (str): name of the problem file
    """
    domain, problem = file_paths(domain, problem)
    data = {'domain': open(domain, 'r').read(),
            'problem': open(problem, 'r').read()}

    req = urllib2.Request('http://solver.planning.domains/solve')
    req.add_header('Content-Type', 'application/json')
    resp = json.loads(urllib2.urlopen(req, json.dumps(data)).read())
    plan = Plan(resp)
    return plan