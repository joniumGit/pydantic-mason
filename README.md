# Mason Models for Pydantic
Pydantic models for Mason Data

See the [Mason Spec](https://github.com/JornWildt/Mason/blob/master/Documentation/Mason-draft-2.md)

#### Summary

Adds mason hypermedia to a pydantic model.
Since this is just a single file you can just copy this into your project.

#### Notes

This will look very ugly in for example FastAPI created OpenAPI schema.
If you use this you want to create custom examples for errors.

#### Usage

```python
from .mason import MasonBase

class MyMason(MasonBase):
    name: str
    age:  int
```

#### Examples

I used these previously in a course project where a Hypermedia app needed to be developed. The code is not the cleanest or clearest perhaps, but should give an idea how these can be used to add Mason capability to an existing API.

- Project: [Book Club](https://github.com/joniumGit/pwp-book-club)
- Models:  [data_models.py](https://github.com/joniumGit/pwp-book-club/blob/0fdb9e2233b9f7b238e8ff6dcdd6ab35cb1e08a4/code/python-api/src/app/data/model/data_models.py)
- Adding Controls: [paths.py](https://github.com/joniumGit/pwp-book-club/blob/0fdb9e2233b9f7b238e8ff6dcdd6ab35cb1e08a4/code/python-api/src/app/resources/paths.py)
- Creating OpenAPI Examples: [doctils.py](https://github.com/joniumGit/pwp-book-club/blob/0fdb9e2233b9f7b238e8ff6dcdd6ab35cb1e08a4/code/python-api/src/app/doc/doctils.py)
