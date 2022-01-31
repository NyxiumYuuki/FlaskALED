import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PageLoginComponent} from "./login/page-login/page-login.component";
import {PageRegisterComponent} from "./register/page-register/page-register.component";
import {PageProfilComponent} from "./common/components/page-profil/page-profil.component";
import {PageUserListComponent} from "./admin/userList/page-user-list/page-user-list.component";
import {PageRegistryComponent} from "./user/page-registry/page-registry.component";
import {UserGuard} from "./common/guards/user/user.guard";
import {AdminGuard} from "./common/guards/admin/admin.guard";

const routes: Routes = [

    { path: "", component: PageLoginComponent },
    { path: "login", component: PageLoginComponent },

    { path: "register", component: PageRegisterComponent },

    { path: "user", component: PageRegistryComponent, canActivate: [UserGuard] },
    { path: "user/registry", component: PageRegistryComponent, canActivate: [UserGuard] },
    { path: "user/myProfil", component: PageProfilComponent, canActivate: [UserGuard] },

    { path: "admin", component: PageUserListComponent, canActivate: [AdminGuard] },
    { path: "admin/userList", component: PageUserListComponent, canActivate: [AdminGuard] },
    { path: "admin/myProfil", component: PageProfilComponent, canActivate: [AdminGuard] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
