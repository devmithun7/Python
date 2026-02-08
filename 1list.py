from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Optional, List


@dataclass
class Node:
    value: Any
    next: Optional["Node"] = None


class SinglyLinkedList:
    """
    Singly Linked List with common operations:
    - insert: at head, tail, index
    - delete: by value, by index, delete head/tail
    - search/contains, get/set by index
    - length, is_empty
    - reverse (in-place)
    - middle node
    - nth from end
    - cycle detection + cycle start
    - remove duplicates
    - to_list / from_iterable
    - clear
    - extend
    """

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

        # "iterable" means "anything you can loop over" (list, tuple, string, range, generator, etc.).
        # If the caller passes one, we append each of its values into this list.
        if iterable is not None:
            self.extend(iterable)

    # -------------------------
    # Basic dunder helpers
    # -------------------------
    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        # "yield" produces values one at a time; this makes the list usable in for-loops.
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __repr__(self) -> str:
        return f"SinglyLinkedList({self.to_list()})"

    def __contains__(self, value: Any) -> bool:
        return self.index_of(value) != -1

    # -------------------------
    # Conversions / utilities
    # -------------------------
    def to_list(self) -> List[Any]:
        return list(iter(self))

    @classmethod
    def from_iterable(cls, it: Iterable[Any]) -> "SinglyLinkedList":
        return cls(it)

    def is_empty(self) -> bool:
        return self._size == 0

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def extend(self, iterable: Iterable[Any]) -> None:
        # This loops over any iterable (like list, string, range, generator, another linked list).
        for x in iterable:
            self.append(x)

    # -------------------------
    # Index validation helpers
    # -------------------------
    def _check_index(self, index: int, allow_end: bool = False) -> None:
        """
        If allow_end=True, index==size is allowed (useful for insert at end).
        """
        if not isinstance(index, int):
            raise TypeError("index must be int")
        max_ok = self._size if allow_end else self._size - 1
        if index < 0 or index > max_ok:
            raise IndexError(f"index out of range: {index}")

    def _node_at(self, index: int) -> Node:
        self._check_index(index)
        cur = self.head
        # cur can't be None because index is valid and size>0
        for _ in range(index):
            assert cur is not None
            cur = cur.next
        assert cur is not None
        return cur

    # -------------------------
    # Insert operations
    # -------------------------
    def prepend(self, value: Any) -> None:
        n = Node(value=value, next=self.head)
        self.head = n
        if self._size == 0:
            self.tail = n
        self._size += 1

    def append(self, value: Any) -> None:
        n = Node(value=value, next=None)
        if self._size == 0:
            self.head = self.tail = n
        else:
            assert self.tail is not None
            self.tail.next = n
            self.tail = n
        self._size += 1

    def insert(self, index: int, value: Any) -> None:
        """
        Insert value at position index (0..size).
        index == size means append.
        """
        self._check_index(index, allow_end=True)
        if index == 0:
            self.prepend(value)
            return
        if index == self._size:
            self.append(value)
            return

        prev = self._node_at(index - 1)
        n = Node(value=value, next=prev.next)
        prev.next = n
        self._size += 1

    # -------------------------
    # Get / Set
    # -------------------------
    def get(self, index: int) -> Any:
        return self._node_at(index).value

    def set(self, index: int, value: Any) -> None:
        self._node_at(index).value = value

    # -------------------------
    # Search
    # -------------------------
    def index_of(self, value: Any) -> int:
        cur = self.head
        i = 0
        while cur is not None:
            if cur.value == value:
                return i
            cur = cur.next
            i += 1
        return -1

    def find(self, value: Any) -> Optional[Node]:
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    # -------------------------
    # Delete / Pop operations
    # -------------------------
    def pop_left(self) -> Any:
        if self._size == 0:
            raise IndexError("pop from empty list")
        assert self.head is not None
        v = self.head.value
        self.head = self.head.next
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return v

    def pop(self) -> Any:
        """
        Pop from tail. O(n) for singly linked list.
        """
        if self._size == 0:
            raise IndexError("pop from empty list")
        if self._size == 1:
            return self.pop_left()

        # find penultimate
        prev = self._node_at(self._size - 2)
        assert self.tail is not None
        v = self.tail.value
        prev.next = None
        self.tail = prev
        self._size -= 1
        return v

    def remove_at(self, index: int) -> Any:
        self._check_index(index)
        if index == 0:
            return self.pop_left()

        prev = self._node_at(index - 1)
        assert prev.next is not None
        target = prev.next
        v = target.value
        prev.next = target.next
        self._size -= 1

        if index == self._size:  # removed last element (size already decremented)
            self.tail = prev
        return v

    def remove(self, value: Any) -> bool:
        """
        Remove first occurrence of value. Returns True if removed.
        """
        if self._size == 0:
            return False

        assert self.head is not None
        if self.head.value == value:
            self.pop_left()
            return True

        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                self._size -= 1
                if cur is self.tail:
                    self.tail = prev
                return True
            prev, cur = cur, cur.next

        return False

    # -------------------------
    # Reverse / helpers
    # -------------------------
    def reverse(self) -> None:
        prev: Optional[Node] = None
        cur = self.head
        self.tail = self.head  # old head becomes tail
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def middle_node(self) -> Optional[Node]:
        """
        Returns the middle node (for even length, returns the second middle).
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def nth_from_end(self, n: int) -> Any:
        """
        n=1 => last element, n=size => first element
        """
        if n <= 0:
            raise ValueError("n must be >= 1")
        if n > self._size:
            raise IndexError("n is larger than list length")

        lead = self.head
        follow = self.head

        for _ in range(n):
            assert lead is not None
            lead = lead.next

        while lead is not None:
            assert follow is not None
            follow = follow.next
            lead = lead.next

        assert follow is not None
        return follow.value

    # -------------------------
    # Duplicate removal (uses set)
    # -------------------------
    def remove_duplicates(self) -> None:
        seen = set()
        prev: Optional[Node] = None
        cur = self.head

        while cur is not None:
            if cur.value in seen:
                assert prev is not None
                prev.next = cur.next
                self._size -= 1
                if cur is self.tail:
                    self.tail = prev
                cur = prev.next
            else:
                seen.add(cur.value)
                prev = cur
                cur = cur.next

    # -------------------------
    # Cycle detection
    # -------------------------
    def has_cycle(self) -> bool:
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def cycle_start(self) -> Optional[Node]:
        """
        If a cycle exists, returns the node where the cycle begins, else None.
        """
        slow = self.head
        fast = self.head

        # Find meeting point
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None  # no cycle

        # Move one pointer to head; step both to find entry
        ptr1 = self.head
        ptr2 = slow
        while ptr1 is not ptr2:
            assert ptr1 is not None and ptr2 is not None
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    ll = SinglyLinkedList([1, 2, 3])
    ll.prepend(0)            # [0,1,2,3]
    ll.append(4)             # [0,1,2,3,4]
    ll.insert(2, 99)         # [0,1,99,2,3,4]
    print(ll)

    print("pop_left:", ll.pop_left())  # removes 0
    print("pop:", ll.pop())            # removes 4
    print("remove 99:", ll.remove(99))
    print("get(1):", ll.get(1))
    ll.set(1, 777)
    print("after set:", ll)

    print("middle:", ll.middle_node().value if ll.middle_node() else None)
    print("2nd from end:", ll.nth_from_end(2))

    ll.reverse()
    print("reversed:", ll)

    ll.extend([2, 2, 3, 3])
    print("with dups:", ll)
    ll.remove_duplicates()
    print("deduped:", ll)
