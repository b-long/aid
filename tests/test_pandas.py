def test_pandas():
    from aid.etl.arbitrary_pandas import do_pandas

    result = do_pandas()
    assert result.shape == (6, 4)
