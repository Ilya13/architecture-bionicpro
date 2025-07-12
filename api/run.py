import uvicorn

uvicorn_args = {
    'host': '0.0.0.0',
    'port': 8000,
    'log_level': 'debug',
}

if __name__ == '__main__':
    uvicorn.run('app.main:app', **uvicorn_args)
