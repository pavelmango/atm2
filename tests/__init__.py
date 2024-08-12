def test_initial_blockchain_state():
    # Определяем, что на начальном этапе блокчейн должен быть пустым
    blockchain = []
    assert len(blockchain) == 0, "Blockchain should be empty on initialization"
