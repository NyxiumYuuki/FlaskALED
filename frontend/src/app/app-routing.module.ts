import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PageLoginComponent} from "./login/page-login/page-login.component";
import {PageRegisterComponent} from "./register/page-register/page-register.component";
import {PageProfilComponent} from "./common/components/page-profil/page-profil.component";
import {PageUserListComponent} from "./admin/userList/page-user-list/page-user-list.component";
import {PageRegistryComponent} from "./user/page-registry/page-registry.component";

const routes: Routes = [

    { path: "", component: PageLoginComponent },
    { path: "login", component: PageLoginComponent },

    { path: "register", component: PageRegisterComponent },

    { path: "user", component: PageRegistryComponent },
    { path: "user/registry", component: PageRegistryComponent },
    { path: "user/myProfil", component: PageProfilComponent },

    { path: "admin", component: PageUserListComponent },
    { path: "admin/userList", component: PageUserListComponent },
    { path: "admin/myProfil", component: PageProfilComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
