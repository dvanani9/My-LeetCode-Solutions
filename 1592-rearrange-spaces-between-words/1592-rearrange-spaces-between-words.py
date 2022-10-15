class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = sum(c.isspace() for c in text)
        if not spaces:
            return text
        words = text.split()
        if len(words) > 1:
            q, r = divmod(spaces, (len(words) - 1))
        else:
            q, r = 0, spaces
        return (" " * q).join(words) + " " * r