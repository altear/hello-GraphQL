# cookbook/ingredients/schema.py
import graphene
import graphql_jwt

from graphene_django.types import DjangoObjectType

from cookbook.ingredients.models import Category, Ingredient, Box


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class BoxType(DjangoObjectType):
    class Meta:
        model = Box

class Query(object):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    all_boxes = graphene.List(BoxType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()

    def resolve_all_boxes(self, info, **kwargs):
        return Box.objects.all()

class Mutation(ingredients.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()