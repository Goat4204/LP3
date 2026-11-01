import heapq

def huffman(freq):
    heap = [[f, [ch, ""]] for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1:]:
            item[1] = "0" + item[1]

        for item in right[1:]:
            item[1] = "1" + item[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    print("Huffman Codes:")
    for ch, code in heap[0][1:]:
        print(ch, ":", code)


text = input("Enter text: ")

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

huffman(freq)
