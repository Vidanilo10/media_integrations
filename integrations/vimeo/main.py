import vimeo

def main() -> int:
    
    client = vimeo.VimeoClient(
        token='e6ba51aef6b19458f2fb8517ea4759ee',
        key='aec0a9d3972becbdfd1b24c19eeb9b3bd760768a',
        secret='FZxBKyocLArY5N7og64zHlA2zuz/VdPyfkRj3nfYDfxfeB6tmlJISBPbb1OsCTUpaxB8KV3hE0cL8jUpQHEo6X1aoxga90F9T//JhHtwW2ug/M/YQytMHRT2WqZY2Q9y'
    )

    response = client.get('https://api.vimeo.com/tutorial')
    print(response.json())
    
    return 0

if __name__ == '__main__':
    main()