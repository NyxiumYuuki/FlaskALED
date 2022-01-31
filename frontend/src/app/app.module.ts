import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PageRegisterComponent } from './register/page-register/page-register.component';
import {FormsModule} from "@angular/forms";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {PageLoginComponent} from "./login/page-login/page-login.component";
import { NavbarComponent } from './common/components/navbar/navbar.component';
import {MatButtonModule} from "@angular/material/button";
import { PageProfilComponent } from './common/components/page-profil/page-profil.component';
import { PopupUpdateProfilComponent } from './common/components/popup-update-profil/popup-update-profil.component';
import {MatDividerModule} from "@angular/material/divider";
import {MatCheckboxModule} from "@angular/material/checkbox";
import {MatDialogModule} from "@angular/material/dialog";
import {MatSnackBarModule} from "@angular/material/snack-bar";
import { PageUserListComponent } from './admin/userList/page-user-list/page-user-list.component';
import { PopupCreatePersonComponent } from './admin/userList/popup-create-person/popup-create-person.component';
import {MatTableModule} from "@angular/material/table";
import {MatPaginatorModule} from "@angular/material/paginator";
import { PopupConfirmRegisterComponent } from './register/popup-confirm-register/popup-confirm-register.component';
import {MatIconModule} from "@angular/material/icon";
import {MatRadioModule} from "@angular/material/radio";
import { PageRegistryComponent } from './user/page-registry/page-registry.component';
import { PopupDeleteProfilComponent } from './common/components/popup-delete-profil/popup-delete-profil.component';
import {MatSortModule} from "@angular/material/sort";
import { PopupUpdatePersonAdminComponent } from './admin/userList/popup-update-person-admin/popup-update-person-admin.component';
import {HttpClientModule} from "@angular/common/http";



@NgModule({
  declarations: [
    AppComponent,
    PageLoginComponent,
    PageRegisterComponent,
    NavbarComponent,
    PageProfilComponent,
    PopupUpdateProfilComponent,
    PageUserListComponent,
    PopupCreatePersonComponent,
    PopupConfirmRegisterComponent,
    PageRegistryComponent,
    PopupDeleteProfilComponent,
    PopupUpdatePersonAdminComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        FormsModule,
        BrowserAnimationsModule,
        HttpClientModule,
        MatFormFieldModule,
        MatInputModule,
        MatButtonModule,
        MatDividerModule,
        MatCheckboxModule,
        MatDialogModule,
        MatSnackBarModule,
        MatTableModule,
        MatPaginatorModule,
        MatSortModule,
        MatIconModule,
        MatRadioModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
