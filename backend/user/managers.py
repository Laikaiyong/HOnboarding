from django.contrib.auth.models import BaseUserManager
from django.db.models import Q
from django.db.models.query import QuerySet


class UserQuerySet(QuerySet):
    def filter_search(self, search):
        return self.filter(
            Q(name__icontains=search)
            | Q(username__icontains=search)
            | Q(email__icontains=search)
        )


class UserManager(BaseUserManager):
    use_in_migrations = True

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db).order_by("role", "username")

    def create_user(self, username, name, email, role, password):
        user = self.model(
            username=username,
            name=name,
            email=self.normalize_email(email),
            role=role,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, name, email, role, password):
        user = self.model(
            username=username,
            name=name,
            email=self.normalize_email(email),
            role=role,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)

        return user