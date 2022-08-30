class Solution:
    def read(self, buf, n):

        total_count = 0
        buf4 = [''] * 4
        while True:
            count = read4(buf4) # reads 4 characters
            buf[total_count:total_count + count] = buf4[:count] # populating buf with characters received in buf4
            total_count += count
            if count < 4 or total_count >= n: # break the loop if end of file is reached or we have received n characters
                break
                
        return total_count if total_count < n else n # since i am adding all the received characters from read4 to buf,
													 # the length of buf might be greater than n. So in that case, return n.