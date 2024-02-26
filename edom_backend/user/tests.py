from .models import Pengguna, Mahasiswa, Professor, EdomAdmin
from django.test import TestCase
from .forms import CreateEdomAdmin


class TestBaseUserModel(TestCase):
    def setUp(self):
        self.user = Pengguna.objects.create_user(
            username="jane.doe",
            full_name="Jane Doe",
            password="sleepyspence1",
        )

    def test_base_user_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), "Jane Doe")

    def test_base_user_get_short_name(self):
        self.assertEqual(self.user.get_short_name(), "jane.doe")

    def test_base_user_string_representation(self):
        self.assertEqual(str(self.user), "jane.doe - Jane Doe")

class TestEdomAdminModel(TestCase):
    def setUp(self) : 
        self.user = Pengguna.objects.create_user(
            username="jane.doe",
            full_name="Jane Doe",
            password="sleepyspence1",
        )
        self.edomadmin = EdomAdmin(user=self.user,id_admin="2022IK")

    def test_admin_get_full_name(self):
        self.assertEqual(self.edomadmin.get_full_name(), "Jane Doe")

    def test_admin_get_short_name(self):
        self.assertEqual(self.edomadmin.get_short_name(), "jane.doe")

    def test_admin_string_representation(self):
        self.assertEqual(str(self.edomadmin), "2022IK - Jane Doe")
    
    def tearDown(self):
        self.edomadmin.delete()
        self.user.delete()

class TestEdomAdminForm(TestCase):
    def test_forms_valid(self):
        self.user = Pengguna.objects.create_user(
            username = "jane.doe",
            full_name="Jane Doe",
            password="sleepyspence1",
        )
        form = CreateEdomAdmin(data = {'user':self.user,'id_admin':'2022IK'})  
        if form.is_valid():
            test_admin = EdomAdmin(user=self.user,id_admin="2022IK")
            test_admin.save()
            self.assertTrue(test_admin.user,self.user)
            

class TestMahasiswaModel(TestCase):
    def setUp(self):
        self.user = Pengguna.objects.create_user(
            username="jane.doe",
            full_name="Jane Doe",
            password="sleepyspence1",
        )
        self.mahasiswa = Mahasiswa.objects.create(user=self.user, npm="1234567890")

    def test_base_mahasiswa_get_full_name(self):
        self.assertEqual(self.mahasiswa.get_full_name(), "Jane Doe")

    def test_base_mahasiswa_get_short_name(self):
        self.assertEqual(self.mahasiswa.get_short_name(), "jane.doe")

    def test_base_mahasiswa_get_npm(self):
        self.assertEqual(self.mahasiswa.get_npm(), "1234567890")

    def test_base_mahasiswa_string_representation(self):
        self.assertEqual(str(self.mahasiswa), "1234567890 - Jane Doe")

    def tearDown(self):
        self.mahasiswa.delete()
        self.user.delete()

class TestProfessorModel(TestCase):
    def setUp(self):
        self.user = Pengguna.objects.create_user(
            username="jane.doe",
            full_name="Jane Doe",
            password="sleepyspence1",
        )
        self.professor = Professor.objects.create(user=self.user, npm="1234567890")

    def test_base_professor_get_full_name(self):
        self.assertEqual(self.professor.get_full_name(), "Jane Doe")

    def test_base_professor_get_short_name(self):
        self.assertEqual(self.professor.get_short_name(), "jane.doe")

    def test_base_professor_get_npm(self):
        self.assertEqual(self.professor.get_npm(), "1234567890")

    def test_base_professor_string_representation(self):
        self.assertEqual(str(self.professor), "1234567890 - Jane Doe")

    def tearDown(self):
        self.professor.delete()
        self.user.delete()
