#main function, check codes
import student_code as sc


def init_map(map_array):
	testmap = []
	for ms in map_array:
		ms_arr = []
		for c in ms:
			ms_arr.append(int(c))
		testmap.append(ms_arr)
	return testmap

def print_map (testmap):
	for lst in testmap:
		print lst
		print '\n'

def check_map_equal (map1, map2):
	flag = True
	for i in range(len(map1)):
		for j in range(len(map1[0])):
			if map1[i][j] != map2[i][j]:
				flag = False
	return flag

def check_score_equal(score1, score2):
	flag = True
	keys1 = score1.keys()
	keys2 = score2.keys()
	if set(keys1) == set(keys2):
		for k in keys1:
			if score1[k] != score2[k]:
				flag = False
	else:
		flag = False
	return flag


def main():
	data1= ["2000000000",
			"0101111111",
			"0100000000",
			"0101111111",
			"0101000001",
			"0101010110",
			"0101010000",
			"0100011110",
			"0011111110",
			"1011111110",
			"1011111111",
			"1000000003"]
	gold_df1 = ["5444444444",
				"5141111111",
				"5144444444",
				"5141111111",
				"5141444441",
				"5141414114",
				"5141414444",
				"5144411114",
				"5511111114",
				"1511111114",
				"1511111111",
				"1555555555"]
					 
	gold_bf1 = ["5444444444",
				"5141111111",
				"5144444444",
				"5141111111",
				"5141444441",
				"5141414110",
				"5141414440",
				"5144411110",
				"5511111110",
				"1511111110",
				"1511111111",
				"1555555555"]
					 

	data2= ["0000000000",
			"1111110101",
			"0300010101",
			"1111010101",
			"0001010101",
			"0100010101",
			"1111010101",
			"0000000101",
			"0111111100",
			"0000000101",
			"0111111120",
			"0000000010"]
				  
	gold_df2 = ["0000005554",
				"1111115151",
				"0555515151",
				"1111515151",
				"4441515151",
				"4144515151",
				"1111515151",
				"4444555151",
				"4111111154",
				"4444444151",
				"4111111154",
				"4444444414"]
					 
	gold_bf2 = ["4444445554",
				"1111115151",
				"0555515151",
				"1111515151",
				"4441515151",
				"4144515151",
				"1111515151",
				"4444555151",
				"4111111154",
				"4440000151",
				"4111111154",
				"4000000014"]

	student_df1 = sc.dfs(init_map(data1))
	if check_map_equal(student_df1, init_map(gold_df1)):
		print "Pass dfs for map1"
	else:
		print "Fail dfs for map1"
		exit(1)

	student_bf1 = sc.bfs(init_map(data1))
	if check_map_equal(student_bf1, init_map(gold_bf1)):
		print "Pass bfs for map1"
	else:
		print "Fail bfs for map1"
		exit(1)

	student_df2 = sc.dfs(init_map(data2))
	if check_map_equal(student_df2, init_map(gold_df2)):
		print "Pass dfs for map2"
	else:
		print "Fail dfs for map2"
		exit(1)

	student_bf2 = sc.bfs(init_map(data2))
	if check_map_equal(student_bf2, init_map(gold_bf2)):
		print "Pass bfs for map2"
	else:
		print "Fail bfs for map2"
		exit(1)

	dis_map = {'Campus': {'Campus': 0, 'Whole_Food': 3, 'Beach': 5, 'Cinema': 5, 'Lighthouse': 1, 'Ryan Field': 2, 'YWCA':12},
				'Whole_Food': {'Campus': 3,  'Whole_Food': 0, 'Beach': 3, 'Cinema': 3, 'Lighthouse': 4, 'Ryan Field': 5, 'YWCA':8},
				'Beach': {'Campus': 5,  'Whole_Food': 3, 'Beach': 0, 'Cinema': 8, 'Lighthouse': 5, 'Ryan Field': 7, 'YWCA':12,},
				'Cinema': {'Campus': 5,  'Whole_Food': 3, 'Beach': 8, 'Cinema': 0, 'Lighthouse': 7, 'Ryan Field': 7, 'YWCA':2},
				'Lighthouse': {'Campus': 1, 'Whole_Food': 4, 'Beach': 5, 'Cinema': 7, 'Lighthouse': 0, 'Ryan Field': 1, 'YWCA':15},
				'Ryan Field': {'Campus': 2, 'Whole_Food': 5, 'Beach': 7, 'Cinema': 7, 'Lighthouse': 1, 'Ryan Field': 0, 'YWCA':12},
				'YWCA': {'Campus': 12, 'Whole_Food': 8, 'Beach': 12, 'Cinema': 2, 'Lighthouse': 15, 'Ryan Field': 12, 'YWCA':0}}
	time_map1 = {'Campus': {'Campus': None, 'Whole_Food': 4, 'Beach': 3, 'Cinema': None, 'Lighthouse': 1, 'Ryan Field': None, 'YWCA': None},
				'Whole_Food': {'Campus': 4,  'Whole_Food': None, 'Beach': 4, 'Cinema': 3, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
				'Beach': {'Campus': 4,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
				'Cinema': {'Campus': None,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': 2},
				'Lighthouse': {'Campus': 1, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': 1, 'YWCA': None},
				'Ryan Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 2, 'Ryan Field': None, 'YWCA': 5},
				'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 3, 'Lighthouse': None, 'Ryan Field': 5, 'YWCA': None}}
	time_map2 = {'Campus': {'Campus': None, 'Whole_Food': 12, 'Beach': 3, 'Cinema': None, 'Lighthouse': 1, 'Ryan Field': None, 'YWCA': None},
				'Whole_Food': {'Campus': 4,  'Whole_Food': None, 'Beach': 4, 'Cinema': 3, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
				'Beach': {'Campus': 4,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': None},
				'Cinema': {'Campus': None,  'Whole_Food': 4, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': None, 'YWCA': 2},
				'Lighthouse': {'Campus': 1, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': None, 'Ryan Field': 1, 'YWCA': None},
				'Ryan Field': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': None, 'Lighthouse': 2, 'Ryan Field': None, 'YWCA': 7},
				'YWCA': {'Campus': None, 'Whole_Food': None, 'Beach': None, 'Cinema': 5, 'Lighthouse': None, 'Ryan Field': 5, 'YWCA': None}}
	student_score1 = sc.a_star_search(dis_map,time_map1, 'Campus', 'Cinema')
	student_score2 = sc.a_star_search(dis_map,time_map2, 'Campus', 'Cinema')
	gold_score1 = {'Whole_Food': {'Beach': 16, 'Campus': 13, 'Cinema': 7}, 'Campus': {'Lighthouse': 8, 'Beach': 11, 'Whole_Food': 7}}
	gold_score2 = {'Ryan Field': {'YWCA': 11, 'Lighthouse': 11}, 'Whole_Food': {'Beach': 19, 'Campus': 16, 'Cinema': 10}, 'Lighthouse': {'Ryan Field': 9, 'Campus': 7}, 'Beach': {'Whole_Food': 10, 'Campus': 12}, 'Campus': {'Lighthouse': 8, 'Beach': 11, 'Whole_Food': 15}}

	if check_score_equal(student_score1,gold_score1):
		print "pass A* search for time map1"
	else:
		print "Fail A* search for time map1"
		exit(1)

	if check_score_equal(student_score2,gold_score2):
		print "pass A* search for time map2"
	else:
		print "Fail A* search for time map2"
		exit(1)
	exit(0)

if __name__== "__main__":
	main()