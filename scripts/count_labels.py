def count_labels(labels):
    counts = {}
    for label in labels:
        counts[label] = counts.get(label,0) + 1
        # counts的第一个键名是cat，如果没有cat就新建，然后给他赋值是获取cat里面他存在的数目，没有就是0，然后都需要加1，最后返回counts
    return counts
    # return counts,list(counts.values()),max(counts, key=counts.get)
    #一共的值和   谁最多 
if __name__ == "__main__":
    print(count_labels(['cat', 'dog', 'cat', 'fish', 'dog', 'dog']))
