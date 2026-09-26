class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''

        path_stack = []
        path_list = path.split('/')

        for item in path_list:
            if item == '.' or item == '':
                continue
            elif item == '..':
                if path_stack:
                    path_stack.pop()
                else:
                    continue
            else:
                path_stack.append(item)

        if not path_stack:
            return '/'
        
        canonical_path = ''
        for item in path_stack:
            canonical_path += '/' + item
        
        return canonical_path
        
        