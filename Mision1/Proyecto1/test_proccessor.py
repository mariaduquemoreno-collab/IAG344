from proccessor import clear_id
def test_clear_id() :
    assert clear_id( "cc-75.087.345" ) == "75087345"

# ================================================

from proccessor import merge_name
def test_merge_name():
    assert merge_name("Cristian", "Correa") == "Cristian Correa"

# ================================================