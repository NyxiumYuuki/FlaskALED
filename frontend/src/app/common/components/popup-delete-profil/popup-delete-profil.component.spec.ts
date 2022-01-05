import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PopupDeleteProfilComponent } from './popup-delete-profil.component';

describe('PopupDeleteProfilComponent', () => {
  let component: PopupDeleteProfilComponent;
  let fixture: ComponentFixture<PopupDeleteProfilComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PopupDeleteProfilComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PopupDeleteProfilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
