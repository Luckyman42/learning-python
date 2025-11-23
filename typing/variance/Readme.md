# Subtypes

`Derived <: Base`

## Invariant

`G` **invariant** if we can't say anything to the releation of `G[Derived]` and `G[Base]` 

> All type in python defaultly invariant 
> `Dog <: Animal`
>
>- `List[Dog]  NOT <:  List[Animal]`
>
>- `List[Animal]  NOT <:  List[Dog]`

[see more](./invariant.py)

## Covariant

`G` **covarient** if `G[Derived] <: G[Base]` 

pl.: Sequence, Tuple, anything which is readonly, or Immutable.

[see more](./covariens_box.py)

## Contravariant

`G` **contravariant** if `G[Base] <: G[Derived]` 


pl.: Function paramters 

```python
def feed_animal(a: Animal): ...
def feed_dog(d: Dog): ...

def handle_dog( feeding : Callable[[Dog],None] ) : ...

handle_dog(feed_animal)  # OK! because you need to handle in the feed_animal that you can get a dog as parameter
```

> So: because of `Dog <: Animal`
> 
> `feed_animal <: feed_dog`


## Overview of python types

| Típus                           | Variance          |
| ------------------------------- | ----------------- |
| `list[T]`                       | **Invariant**     |
| `dict[K, V]`                    | **Invariant**     |
| `set[T]`                        | **Invariant**     |
| `tuple[T, ...]`                 | **Covariant**     |
| `Sequence[T]`                   | **Covariant**     |
| `Iterable[T]`                   | **Covariant**     |
| `Callable[[T], R]` for input T  | **Contravariant** |
| `Callable[[T], R]` for output R | **Covariant**     |
