mod ref_cell {
    use std::{
        cell::{Cell, UnsafeCell},
        ops::{Deref, DerefMut},
    };

    pub struct RefCell<T: ?Sized> {
        ref_cnt: Cell<i32>,
        unsafe_cell: UnsafeCell<T>,
    }

    impl<T> RefCell<T> {
        pub fn new(value: T) -> Self {
            Self {
                ref_cnt: Cell::new(0),
                unsafe_cell: UnsafeCell::new(value),
            }
        }
        pub fn borrow(&self) -> Ref<'_, T> {
            assert!(self.ref_cnt.get() >= 0, "Mut borrowed");
            self.ref_cnt.set(self.ref_cnt.get() + 1);
            Ref {
                ref_cnt: &self.ref_cnt,
                value: unsafe { &*self.unsafe_cell.get() },
            }
        }
        pub fn borrow_mut(&self) -> RefMut<'_, T> {
            assert!(self.ref_cnt.get() == 0, "Borrowed");
            self.ref_cnt.set(-1);
            RefMut {
                ref_cnt: &self.ref_cnt,
                value: unsafe { &mut *self.unsafe_cell.get() },
            }
        }
    }

    pub struct Ref<'a, T> {
        ref_cnt: &'a Cell<i32>,
        value: &'a T,
    }
    impl<'a, T> Drop for Ref<'a, T> {
        fn drop(&mut self) {
            self.ref_cnt.set(self.ref_cnt.get() - 1);
        }
    }
    impl<'a, T> Deref for Ref<'a, T> {
        type Target = T;

        fn deref(&self) -> &Self::Target {
            self.value
        }
    }
    pub struct RefMut<'a, T> {
        ref_cnt: &'a Cell<i32>,
        value: &'a mut T,
    }
    impl<'a, T> Drop for RefMut<'a, T> {
        fn drop(&mut self) {
            self.ref_cnt.set(0);
        }
    }
    impl<'a, T> Deref for RefMut<'a, T> {
        type Target = T;

        fn deref(&self) -> &Self::Target {
            self.value
        }
    }
    impl<'a, T> DerefMut for RefMut<'a, T> {
        fn deref_mut(&mut self) -> &mut Self::Target {
            self.value
        }
    }
}

fn main() {
    use ref_cell::RefCell;
    let rc = RefCell::new(String::from("Holy Moses"));
    let mut r = rc.borrow();
    let mut rm = rc.borrow_mut();
    rm.push('!');
    println!("{}", *rc.borrow());
}
