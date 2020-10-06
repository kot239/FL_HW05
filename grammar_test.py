import pytest
from parser import parse_file

def test_simple1():
	assert parse_file('test_files/simple1.txt')

def test_simple2():
	assert parse_file('test_files/simple2.txt')

def test_simple3():
	assert parse_file('test_files/simple3.txt')

def test_simple_error1():
	assert not parse_file('test_files/simple_error1.txt')

def test_simple_error2():
	assert not parse_file('test_files/simple_error2.txt')

def test_simple_error3():
	assert not parse_file('test_files/simple_error3.txt')

def test_simple_error4():
	assert not parse_file('test_files/simple_error4.txt')

def test_simple_error5():
	assert not parse_file('test_files/simple_error5.txt')

def test_simple_error6():
	assert not parse_file('test_files/simple_error6.txt')

def test_simple_error7():
	assert not parse_file('test_files/simple_error7.txt')

def test_simple_error8():
	assert not parse_file('test_files/simple_error8.txt')

def test_empty():
	assert parse_file('test_files/empty.txt')

def test_with_empty_lines():
	assert parse_file('test_files/empty_lines.txt')

def test_parentheses():
	assert parse_file('test_files/parentheses.txt')

def test_without_spaces():
	assert parse_file('test_files/antispace.txt')

def test_lexer_error1():
	assert not parse_file('test_files/lexer_error1.txt')

def test_lexer_error2():
	assert not parse_file('test_files/lexer_error2.txt')

def test_lexer_error3():
	assert not parse_file('test_files/lexer_error3.txt')

def test_rick_astley():
	assert parse_file('test_files/rick_astley.txt')

def test_simple_new1():
	assert parse_file('test_files/simple_new1.txt')

def test_simple_new2():
	assert parse_file('test_files/simple_new2.txt')

def test_simple_new3():
	assert parse_file('test_files/simple_new3.txt')

def test_simple_new4():
	assert parse_file('test_files/simple_new4.txt')

def test_simple_new_error1():
	assert not parse_file('test_files/simple_new_error1.txt')

def test_simple_new_error2():
	assert not parse_file('test_files/simple_new_error2.txt')

def test_simple_new_error3():
	assert not parse_file('test_files/simple_new_error3.txt')

def test_simple_new_error4():
	assert not parse_file('test_files/simple_new_error4.txt')

def test_simple_new_error5():
	assert not parse_file('test_files/simple_new_error5.txt')

def test_simple_new_error6():
	assert not parse_file('test_files/simple_new_error6.txt')
