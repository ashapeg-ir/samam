import graphene
from graphene_django import DjangoObjectType

from modules.palace.models import Department, Palace


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Palace
        fields = ["id", "city", "name", "parent"]


class DepartmentType(DjangoObjectType):

    class Meta:
        model = Department
        fields = ["id", "name", "description"]


class Query(graphene.ObjectType):
    all_organizations = graphene.List(OrganizationType)
    departments = graphene.List(DepartmentType)

    def resolve_all_organizations(self, root):
        return Organization.objects.all()


schema = graphene.Schema(query=Query)
