import heapq

def huffman(characters, freq):
    heap = [[freq[i], characters[i]] for i in range(len(characters))]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, [left[0] + right[0], left[1] + right[1]])
    print("Huffman Tree:", heap[0])

characters = list(input("Enter characters: "))
freq = list(map(int, input("Enter frequencies: ").split()))
huffman(characters, freq)