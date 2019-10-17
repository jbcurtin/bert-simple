from bert import binding, utils, constants

@binding.follow('noop')
def first_aws_lambda_function():
    work_queue, done_queue, ologger = utils.comm_binders(first_aws_lambda_function)
    ologger.info('Awesome')
    for idx in range(0, 10):
        work_queue.put({'idx': idx})


@binding.follow(first_aws_lambda_function)
def second_aws_lambda_function():
    work_queue, done_queue, ologger = utils.comm_binders(second_aws_lambda_function)
    for details in work_queue:
        idx = details['idx']
        ologger.info(f'IDX: {idx}')

