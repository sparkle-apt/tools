def _split_multi_line_sql(script, sep=';'):
    """
    Split multi-line sql script by ``sep``
    
    :param str script:
    :param str sep:
    
    :return: list of sql
    """
    
#     res = script.replace('\n', ' ')
    res = script.split(sep)
    # filter empty line
    res = [item.strip() for item in res]
    res = [item for item in res if item and not item.startswith('--')]
    
    return res
        
def sql_from_str(redshift_hook, script, verbose=True):
    """
    :param redshift_hook:
    :param str script: sql script
    
    :return: Pandas.DataFrame or None in case no data is returned
    """
    res = None
    lines = _split_multi_line_sql(script)
    for line in lines:
        if verbose:
            print('********START********')
            print(line)
            print('********END********')
        try:
            res = redshift_hook.get_pandas_df(line)
        except Exception as e:
            print(e)
        
    return res
        
def sql_from_file(redshift_hook, file_path, verbose=True):
    """
    :param redshift_hook:
    :param str file_path: path of script path
    
    :return: Pandas.DataFrame or None in case no data is returned
    """
    res = None
    try:
        with open(file_path, 'r') as f:
            script = f.read()
            res = sql_from_str(redshift_hook, script, verbose=verbose)
    except Exception as e:
        print(e)
        
    return res