import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PopupUpdateProfilComponent } from './popup-update-profil.component';

describe('PopupModifierUtilisateurComponent', () => {
  let component: PopupUpdateProfilComponent;
  let fixture: ComponentFixture<PopupUpdateProfilComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PopupUpdateProfilComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PopupUpdateProfilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
