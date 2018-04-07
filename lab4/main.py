import planner

def main():
	## Test 0
	plan = planner.find_plan("student_domain.pddl", "task00.pddl")
	print "Test 0"
	if plan.ok:
		print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 1 and len(plan.plan) < 4:
			print "Pass Test 0"
		else:
			print "Fail Test 0"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 0"
		exit(1)

	## Test 1
	plan = planner.find_plan("student_domain.pddl", "task01.pddl")
	print "Test 1"
	if plan.ok:
		print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 2:
			print "Pass Test 1"
		else:
			print "Fail Test 1"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 1"
		exit(1)

	## Test 2
	plan = planner.find_plan("student_domain.pddl", "task02.pddl")
	print "Test 2"
	if plan.ok:
		print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 2 and len(plan.plan) < 10:
			print "Pass Test 2"
		else:
			print "Fail Test 2"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 2"
		exit(1)

	## Test 3
	plan = planner.find_plan("student_domain.pddl", "task03.pddl")
	print "Test 3"
	if plan.ok:
		print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 4 and len(plan.plan) < 18:
			print "Pass Test 3"
		else:
			print "Fail Test 3"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 3"
		exit(1)

	## Test 4
	plan = planner.find_plan("student_domain.pddl", "task04.pddl")
	print "Test 4"
	if plan.ok:
		print '\n'.join(a for a in plan.plan)
		if len(plan.plan) > 1 and len(plan.plan) < 4:
			print "Pass Test 4"
		else:
			print "Fail Test 4"
			exit(1)
	else:
		print "ERROR"
		print plan.error
		print "Fail Test 4"
		exit(1)
		


if __name__ == '__main__':
    main()
