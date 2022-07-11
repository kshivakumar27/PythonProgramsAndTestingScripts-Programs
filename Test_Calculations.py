#from day4 import Calculations as ca

import sys
import Calculations as ca

import pytest
from Calculations import ca



def test_sub():
    assert ca.sub(9,8) == 1



def test_add():
    assert ca.add(3,4) == 7



def test_addstrings():
    assert ca.add('a','b') == 'abq'






#############################







def test_validate_age():
    ca.validate_age(19)



def test_validate_age_one():
    ca.validate_age(13)



def test_validate_message():
    with pytest.raises(ValueError) as e:
        ca.validate_age(11)
    assert str(e.value) == "age is less, cannot vote."




# pytest markers



def test_sub():
    assert ca.sub(9,8) == 1



@pytest.mark.skip(reason = "just to give demo")
def test_addstrings():
    assert ca.add('a','b') == 'abq'



@pytest.mark.skip(reason = "adding demo")
def test_add():
    assert ca.add(3,4) == 7



@pytest.mark.skipif(sys.version_info < (3,7), reason = "my version is greater 3.7")
def test_add_one():
    assert ca.add(3,4) == 7



##################---------------------------------------
# pytest markers



@pytest.mark.parametrize("a,b,res",[(3,4,7), ('a','b','ab'),(5,6,10)])
def test_myadd(a,b,res):
    assert ca.add(a,b) == res



#################3-------------------------------------------------




################Fixtures





import pytest




@pytest.fixture()
def db_details():
    name = "ansari"
    phone = 123456
    age = 45
    return [name,phone,age]



def test_name(db_details):
    res = 'abdul'
    assert db_details[0] == res



def test_phone(db_details):
    res = 123456
    assert db_details[1] == res
