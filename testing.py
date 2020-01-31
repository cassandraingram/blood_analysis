def test_HDL_analysis(): 
	from chol_analysis import HDL_analysis
	answer = HDL_analysis(80)
	expected = "normal"
	assert answer == expected

def test_HDL_analysis():
	from chol_analysis import HDL_analysis
	answer = HDL_analysis(40)
	expected = "borderline low"
	assert answer == expected